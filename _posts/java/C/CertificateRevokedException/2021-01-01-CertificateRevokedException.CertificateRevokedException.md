---
title: CertificateRevokedException.CertificateRevokedException()
permalink: Java/CertificateRevokedException/CertificateRevokedException
date: 2021-01-11
key: JavaJava.C.CertificateRevokedException
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateRevokedException.constructores valor="CertificateRevokedException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CertificateRevokedException(Date revocationDate, CRLReason reason, X500Principal authority, Map<String,Extension> extensions)
~~~

## Parámetros
* **Date revocationDate**,  {% include w3api/param_description.html metodo=_dato parametro="Date revocationDate" %}
* **CRLReason reason**,  {% include w3api/param_description.html metodo=_dato parametro="CRLReason reason" %}
* **Extension&gt; extensions**,  {% include w3api/param_description.html metodo=_dato parametro="Extension> extensions" %}
* **X500Principal authority**,  {% include w3api/param_description.html metodo=_dato parametro="X500Principal authority" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CertificateRevokedException](/Java/CertificateRevokedException/)

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
