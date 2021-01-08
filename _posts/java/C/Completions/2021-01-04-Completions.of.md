---
title: Completions.of()
permalink: Java/Completions/of
date: 2021-01-04
key: JavaJava.C.Completions
category: java
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
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}

## Clase Padre
[Completions](/Java/Completions/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Completions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
