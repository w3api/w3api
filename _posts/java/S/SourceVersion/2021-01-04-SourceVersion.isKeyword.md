---
title: SourceVersion.isKeyword()
permalink: Java/SourceVersion/isKeyword
date: 2021-01-04
key: JavaJava.S.SourceVersion
category: java
tags: ['java se', 'javax.lang.model', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceVersion.metodos valor="isKeyword" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isKeyword(CharSequence s)
public static boolean isKeyword(CharSequence s, SourceVersion version)
~~~

## Parámetros
* **SourceVersion version**,  {% include w3api/param_description.html metodo=_data parametro="SourceVersion version" %}
* **CharSequence s**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence s" %}

## Clase Padre
[SourceVersion](/Java/SourceVersion/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SourceVersion.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
