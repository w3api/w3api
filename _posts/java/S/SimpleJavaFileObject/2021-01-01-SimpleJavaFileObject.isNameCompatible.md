---
title: SimpleJavaFileObject.isNameCompatible()
permalink: Java/SimpleJavaFileObject/isNameCompatible
date: 2021-01-11
key: JavaJava.S.SimpleJavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleJavaFileObject.metodos valor="isNameCompatible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isNameCompatible(String simpleName, JavaFileObject.Kind kind)
~~~

## Parámetros
* **String simpleName**,  {% include w3api/param_description.html metodo=_dato parametro="String simpleName" %}
* **JavaFileObject.Kind kind**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject.Kind kind" %}

## Clase Padre
[SimpleJavaFileObject](/Java/SimpleJavaFileObject/)

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
