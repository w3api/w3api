---
title: Diagnostic.Kind.valueOf()
permalink: Java/Diagnostic/Kind-javax-tools/valueOf
date: 2021-01-11
key: JavaJava.D.Diagnostic.Kind-javax-tools
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.Diagnostic.Kind-javax-tools.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Diagnostic.Kind valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Diagnostic.Kind](/Java/Diagnostic/Kind-javax-tools/)

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
