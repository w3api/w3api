---
title: SimpleJavaFileObject.SimpleJavaFileObject()
permalink: Java/SimpleJavaFileObject/SimpleJavaFileObject
date: 2021-01-04
key: JavaJava.S.SimpleJavaFileObject
category: java
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
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}
* **JavaFileObject.Kind kind**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileObject.Kind kind" %}

## Clase Padre
[SimpleJavaFileObject](/Java/SimpleJavaFileObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleJavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
