---
title: PixelFormat.createByteIndexedInstance()
permalink: /Java/PixelFormat/createByteIndexedInstance/
date: 2021-01-11
key: Java.P.PixelFormat
category: Java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelFormat.metodos valor="createByteIndexedInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static PixelFormat<ByteBuffer> createByteIndexedInstance(int[] colors)
~~~

## Parámetros
* **int[] colors**,  {% include w3api/param_description.html metodo=_dato parametro="int[] colors" %}

## Clase Padre
[PixelFormat](/Java/PixelFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
