---
title: StyleConverter.readBinary()
permalink: Java/StyleConverter/readBinary
date: 2021-01-11
key: JavaJava.S.StyleConverter
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleConverter.metodos valor="readBinary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static StyleConverter<?,?> readBinary(DataInputStream is, String[] strings) throws IOException
~~~

## Parámetros
* **DataInputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="DataInputStream is" %}
* **String[] strings**,  {% include w3api/param_description.html metodo=_dato parametro="String[] strings" %}

## Excepciones
[IOException](/Java/IOException/)

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
