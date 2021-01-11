---
title: MessageFormat.setFormat()
permalink: Java/MessageFormat/setFormat
date: 2021-01-11
key: JavaJava.M.MessageFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFormat.metodos valor="setFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFormat(int formatElementIndex, Format newFormat)
~~~

## Parámetros
* **int formatElementIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int formatElementIndex" %}
* **Format newFormat**,  {% include w3api/param_description.html metodo=_dato parametro="Format newFormat" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[MessageFormat](/Java/MessageFormat/)

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
