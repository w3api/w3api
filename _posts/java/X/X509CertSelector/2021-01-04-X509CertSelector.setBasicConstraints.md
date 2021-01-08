---
title: X509CertSelector.setBasicConstraints()
permalink: Java/X509CertSelector/setBasicConstraints
date: 2021-01-04
key: JavaJava.X.X509CertSelector
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setBasicConstraints" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setBasicConstraints(int minMaxPathLen)
~~~

## Parámetros
* **int minMaxPathLen**,  {% include w3api/param_description.html metodo=_data parametro="int minMaxPathLen" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
