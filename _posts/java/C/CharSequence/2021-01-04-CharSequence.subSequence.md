---
title: CharSequence.subSequence()
permalink: Java/CharSequence/subSequence
date: 2021-01-04
key: JavaJava.C.CharSequence
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharSequence.metodos valor="subSequence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CharSequence subSequence(int start, int end)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CharSequence](/Java/CharSequence/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CharSequence.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
