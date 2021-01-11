---
title: SourceVersion.isName()
permalink: Java/SourceVersion/isName
date: 2021-01-11
key: JavaJava.S.SourceVersion
category: java
tags: ['java se', 'javax.lang.model', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SourceVersion.metodos valor="isName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isName(CharSequence name)
public static boolean isName(CharSequence name, SourceVersion version)
~~~

## Parámetros
* **CharSequence name**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence name" %}
* **SourceVersion version**,  {% include w3api/param_description.html metodo=_dato parametro="SourceVersion version" %}

## Clase Padre
[SourceVersion](/Java/SourceVersion/)

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
