---
title: X509CertSelector.setSubjectAlternativeNames()
permalink: Java/X509CertSelector/setSubjectAlternativeNames
date: 2021-01-04
key: JavaJava.X.X509CertSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setSubjectAlternativeNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSubjectAlternativeNames(Collection<List<?>> names) throws IOException
~~~

## Parámetros
* **Collection&lt;List&lt;?&gt;&gt; names**,  {% include w3api/param_description.html metodo=_data parametro="Collection<List<?>> names" %}

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
