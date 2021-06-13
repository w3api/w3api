---
title: SimpleJavaFileObject.SimpleJavaFileObject()
permalink: /Java/SimpleJavaFileObject/SimpleJavaFileObject/
date: 2021-01-11
key: Java.S.SimpleJavaFileObject
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleJavaFileObject.constructores valor="SimpleJavaFileObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SimpleJavaFileObject(URI uri, JavaFileObject.Kind kind)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}
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
