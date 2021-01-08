---
title: DocletEnvironment.getFileKind()
permalink: Java/DocletEnvironment/getFileKind
date: 2021-01-04
key: JavaJava.D.DocletEnvironment
category: java
tags: ['java se', 'jdk.javadoc.doclet', 'jdk.javadoc', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocletEnvironment.metodos valor="getFileKind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaFileObject.Kind getFileKind(TypeElement type)
~~~

## Parámetros
* **TypeElement type**,  {% include w3api/param_description.html metodo=_data parametro="TypeElement type" %}

## Clase Padre
[DocletEnvironment](/Java/DocletEnvironment/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocletEnvironment.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
