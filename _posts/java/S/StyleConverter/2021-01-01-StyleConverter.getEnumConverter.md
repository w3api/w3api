---
title: StyleConverter.getEnumConverter()
permalink: Java/StyleConverter/getEnumConverter
date: 2021-01-11
key: JavaJava.S.StyleConverter
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleConverter.metodos valor="getEnumConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <E extends Enum<E>>StyleConverter<String,? extends Enum<?>> getEnumConverter(Class<E> enumClass)
~~~

## Parámetros
* **Class&lt;E&gt; enumClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<E> enumClass" %}

## Clase Padre
[StyleConverter](/Java/StyleConverter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
