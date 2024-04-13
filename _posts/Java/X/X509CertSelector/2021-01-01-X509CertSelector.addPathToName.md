---
title: X509CertSelector.addPathToName()
permalink: /Java/X509CertSelector/addPathToName/
date: 2021-01-11
key: Java.X.X509CertSelector
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="addPathToName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addPathToName(int type, byte[] name) throws IOException
public void addPathToName(int type, String name) throws IOException
~~~

## Parámetros
* **byte[] name**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] name" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
