---
title: X509CertSelector.setSubjectPublicKey()
permalink: /Java/X509CertSelector/setSubjectPublicKey/
date: 2021-01-11
key: Java.X.X509CertSelector
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setSubjectPublicKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSubjectPublicKey(byte[] key) throws IOException
public void setSubjectPublicKey(PublicKey key)
~~~

## Parámetros
* **byte[] key**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] key" %}
* **PublicKey key**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey key" %}

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
