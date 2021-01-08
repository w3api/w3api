---
title: Timestamp.Timestamp()
permalink: Java/Timestamp-java-security/Timestamp
date: 2021-01-04
key: JavaJava.T.Timestamp-java-security
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Timestamp-java-security.constructores valor="Timestamp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Timestamp(Date timestamp, CertPath signerCertPath)
~~~

## Parámetros
* **Date timestamp**,  {% include w3api/param_description.html metodo=_data parametro="Date timestamp" %}
* **CertPath signerCertPath**,  {% include w3api/param_description.html metodo=_data parametro="CertPath signerCertPath" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Timestamp](/Java/Timestamp-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Timestamp-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
