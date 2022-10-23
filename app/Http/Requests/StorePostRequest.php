<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePostRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, mixed>
     */
    public function rules()
    {
        return [
            'content' => 'required',
            'category_id' => 'required|integer',
        ];
    }

    public function messages()
    {
        return [
            'content.required' => 'Nội dung bài viết không được để trống',
            'category_id.required' => 'Danh mục không được để trống',
            'category_id.integer' => 'Danh mục không hợp lệ',
        ];
    }
}
