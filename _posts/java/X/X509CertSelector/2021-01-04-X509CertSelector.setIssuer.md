---
title: X509CertSelector.setIssuer()
permalink: Java/X509CertSelector/setIssuer
date: 2021-01-04
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
* **String issuerDN**,  {% include w3api/param_description.html metodo=_data parametro="String issuerDN" %}
* **byte[] issuerDN**,  {% include w3api/param_description.html metodo=_data parametro="byte[] issuerDN" %}
* **X500Principal issuer**,  {% include w3api/param_description.html metodo=_data parametro="X500Principal issuer" %}

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
