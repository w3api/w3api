---
title: ChoiceFormat.parse()
permalink: Java/ChoiceFormat/parse
date: 2021-01-11
key: JavaJava.C.ChoiceFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceFormat.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Number parse(String text, ParsePosition status)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **ParsePosition status**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition status" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ChoiceFormat](/Java/ChoiceFormat/)

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
