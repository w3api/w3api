---
title: ForwardingJavaFileManager.getClassLoader()
permalink: /Java/ForwardingJavaFileManager/getClassLoader/
date: 2021-01-11
key: Java.F.ForwardingJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="getClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ClassLoader getClassLoader(JavaFileManager.Location location)
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/)

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
