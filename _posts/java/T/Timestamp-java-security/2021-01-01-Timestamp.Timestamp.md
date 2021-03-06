---
title: Timestamp.Timestamp()
permalink: /Java/Timestamp-java-security/Timestamp/
date: 2021-01-11
key: Java.T.Timestamp-java-security
category: Java
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
* **Date timestamp**,  {% include w3api/param_description.html metodo=_dato parametro="Date timestamp" %}
* **CertPath signerCertPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath signerCertPath" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
