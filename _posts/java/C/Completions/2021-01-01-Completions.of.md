---
title: Completions.of()
permalink: /Java/Completions/of/
date: 2021-01-11
key: Java.C.Completions
category: Java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Completions.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Completion of(String value)
public static Completion of(String value, String message)
~~~

## Parámetros
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[Completions](/Java/Completions/)

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
