---
title: X509CertSelector.setExtendedKeyUsage()
permalink: Java/X509CertSelector/setExtendedKeyUsage
date: 2021-01-11
key: JavaJava.X.X509CertSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setExtendedKeyUsage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setExtendedKeyUsage(Set<String> keyPurposeSet) throws IOException
~~~

## Parámetros
* **Set&lt;String&gt; keyPurposeSet**,  {% include w3api/param_description.html metodo=_dato parametro="Set<String> keyPurposeSet" %}

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
