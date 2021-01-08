---
title: X509CertSelector.addSubjectAlternativeName()
permalink: Java/X509CertSelector/addSubjectAlternativeName
date: 2021-01-04
key: JavaJava.X.X509CertSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="addSubjectAlternativeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addSubjectAlternativeName(int type, byte[] name) throws IOException
public void addSubjectAlternativeName(int type, String name) throws IOException
~~~

## Parámetros
* **byte[] name**,  {% include w3api/param_description.html metodo=_data parametro="byte[] name" %}
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[X509CertSelector](/Java/X509CertSelector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509CertSelector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
