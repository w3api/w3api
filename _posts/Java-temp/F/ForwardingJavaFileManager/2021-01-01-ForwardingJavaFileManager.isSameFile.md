---
title: ForwardingJavaFileManager.isSameFile()
permalink: /Java/ForwardingJavaFileManager/isSameFile/
date: 2021-01-11
key: Java.F.ForwardingJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="isSameFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isSameFile(FileObject a, FileObject b)
~~~

## Parámetros
* **FileObject a**,  {% include w3api/param_description.html metodo=_dato parametro="FileObject a" %}
* **FileObject b**,  {% include w3api/param_description.html metodo=_dato parametro="FileObject b" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ForwardingJavaFileManager](/Java/ForwardingJavaFileManager/)

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
