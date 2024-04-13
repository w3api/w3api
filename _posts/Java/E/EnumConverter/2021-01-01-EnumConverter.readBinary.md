---
title: EnumConverter.readBinary()
permalink: /Java/EnumConverter/readBinary/
date: 2021-01-11
key: Java.E.EnumConverter
category: Java
tags: ['java se', 'javafx.css.converter', 'javafx.graphics', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EnumConverter.metodos valor="readBinary" %}

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
[EnumConverter](/Java/EnumConverter/)

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
