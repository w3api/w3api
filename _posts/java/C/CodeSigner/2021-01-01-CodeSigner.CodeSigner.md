---
title: CodeSigner.CodeSigner()
permalink: /Java/CodeSigner/CodeSigner/
date: 2021-01-11
key: Java.C.CodeSigner
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CodeSigner.constructores valor="CodeSigner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CodeSigner(CertPath signerCertPath, Timestamp timestamp)
~~~

## Parámetros
* **Timestamp timestamp**,  {% include w3api/param_description.html metodo=_dato parametro="Timestamp timestamp" %}
* **CertPath signerCertPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath signerCertPath" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CodeSigner](/Java/CodeSigner/)

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
