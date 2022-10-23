<?php

namespace App\Http\Controllers;

use App\Models\Post;
use App\Http\Requests\StorePostRequest;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;

class PostController extends Controller
{
    public function index(Request $request)
    {
        $posts = Post::query();

        if (!empty($request->keyword)) {
            $posts->where('content', 'like', '%' . $request->keyword . '%');
        }

        if (!empty($request->category_id)) {
            $posts->withWhereHas('category', function ($q) use ($request) {
                return $q->where('id', $request->category_id);
            });
        }

        $posts = $posts->paginate(10);

        return response()->json([
            'success' => true,
            'data' => $posts
        ], 200);
    }

    public function store(StorePostRequest $request)
    {
        Post::create([
            'content' => $request->content,
            'category_id' => $request->category_id,
            'user_id' => Auth::user()->id,
        ]);

        return response()->json([
            'success' => true,
            'message' => 'Thêm mới bài viết thành công'
        ], 200);
    }
}
