---
title: ForwardingJavaFileManager.inferBinaryName()
permalink: Java/ForwardingJavaFileManager/inferBinaryName
date: 2021-01-11
key: JavaJava.F.ForwardingJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForwardingJavaFileManager.metodos valor="inferBinaryName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String inferBinaryName(JavaFileManager.Location location, JavaFileObject file)
~~~

## Parámetros
* **JavaFileObject file**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject file" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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
