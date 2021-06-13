---
title: PKIXRevocationChecker.setOcspResponses()
permalink: /Java/PKIXRevocationChecker/setOcspResponses/
date: 2021-01-11
key: Java.P.PKIXRevocationChecker
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXRevocationChecker.metodos valor="setOcspResponses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setOcspResponses(Map<X509Certificate,byte[]> responses)
~~~

## Parámetros
* **byte[]&gt; responses**,  {% include w3api/param_description.html metodo=_dato parametro="byte[]> responses" %}
* **Map&lt;X509Certificate**,  {% include w3api/param_description.html metodo=_dato parametro="Map<X509Certificate" %}

## Clase Padre
[PKIXRevocationChecker](/Java/PKIXRevocationChecker/)

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
