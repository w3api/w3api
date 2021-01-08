---
title: ForwardingJavaFileManager.contains()
permalink: Java/ForwardingJavaFileManager/contains
date: 2021-01-04
key: JavaJava.F.ForwardingJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="contains" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean contains(JavaFileManager.Location location, FileObject fo) throws IOException
~~~

## Parámetros
* **FileObject fo**,  {% include w3api/param_description.html metodo=_data parametro="FileObject fo" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ForwardingJavaFileManager](/Java/ForwardingJavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForwardingJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
