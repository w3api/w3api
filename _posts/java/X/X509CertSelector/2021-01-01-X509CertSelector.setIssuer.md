---
title: X509CertSelector.setIssuer()
permalink: Java/X509CertSelector/setIssuer
date: 2021-01-11
key: JavaJava.X.X509CertSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setIssuer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setIssuer(byte[] issuerDN) throws IOException
public void setIssuer(String issuerDN) throws IOException
public void setIssuer(X500Principal issuer)
~~~

## Parámetros
* **String issuerDN**,  {% include w3api/param_description.html metodo=_dato parametro="String issuerDN" %}
* **X500Principal issuer**,  {% include w3api/param_description.html metodo=_dato parametro="X500Principal issuer" %}
* **byte[] issuerDN**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] issuerDN" %}

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
