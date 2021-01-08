---
title: CodeSource.CodeSource()
permalink: Java/CodeSource/CodeSource
date: 2021-01-04
key: JavaJava.C.CodeSource
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CodeSource.constructores valor="CodeSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CodeSource(URL url, Certificate[] certs)
public CodeSource(URL url, CodeSigner[] signers)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **CodeSigner[] signers**,  {% include w3api/param_description.html metodo=_data parametro="CodeSigner[] signers" %}
* **Certificate[] certs**,  {% include w3api/param_description.html metodo=_data parametro="Certificate[] certs" %}

## Clase Padre
[CodeSource](/Java/CodeSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CodeSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
