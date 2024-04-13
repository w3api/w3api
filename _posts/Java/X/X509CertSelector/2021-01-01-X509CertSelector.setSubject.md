---
title: X509CertSelector.setSubject()
permalink: /Java/X509CertSelector/setSubject/
date: 2021-01-11
key: Java.X.X509CertSelector
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setSubject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSubject(byte[] subjectDN) throws IOException
public void setSubject(String subjectDN) throws IOException
public void setSubject(X500Principal subject)
~~~

## Parámetros
* **X500Principal subject**,  {% include w3api/param_description.html metodo=_dato parametro="X500Principal subject" %}
* **String subjectDN**,  {% include w3api/param_description.html metodo=_dato parametro="String subjectDN" %}
* **byte[] subjectDN**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] subjectDN" %}

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
