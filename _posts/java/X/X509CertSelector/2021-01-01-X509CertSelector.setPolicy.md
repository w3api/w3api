---
title: X509CertSelector.setPolicy()
permalink: /Java/X509CertSelector/setPolicy/
date: 2021-01-11
key: Java.X.X509CertSelector
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509CertSelector.metodos valor="setPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPolicy(Set<String> certPolicySet) throws IOException
~~~

## Parámetros
* **Set&lt;String&gt; certPolicySet**,  {% include w3api/param_description.html metodo=_dato parametro="Set<String> certPolicySet" %}

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
