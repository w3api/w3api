---
title: X509CRLSelector.addIssuerName()
permalink: Java/X509CRLSelector/addIssuerName
date: 2021-01-11
key: JavaJava.X.X509CRLSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CRLSelector.metodos valor="addIssuerName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addIssuerName(byte[] name) throws IOException
public void addIssuerName(String name) throws IOException
~~~

## Parámetros
* **byte[] name**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] name" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[X509CRLSelector](/Java/X509CRLSelector/)

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
