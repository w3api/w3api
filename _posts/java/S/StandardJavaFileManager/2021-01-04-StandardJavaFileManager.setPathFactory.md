---
title: StandardJavaFileManager.setPathFactory()
permalink: Java/StandardJavaFileManager/setPathFactory
date: 2021-01-04
key: JavaJava.S.StandardJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="setPathFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void setPathFactory(StandardJavaFileManager.PathFactory f)
~~~

## Parámetros
* **StandardJavaFileManager.PathFactory f**,  {% include w3api/param_description.html metodo=_data parametro="StandardJavaFileManager.PathFactory f" %}

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
