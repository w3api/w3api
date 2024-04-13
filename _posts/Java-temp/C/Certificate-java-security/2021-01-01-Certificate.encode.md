---
title: Certificate.encode()
permalink: /Java/Certificate-java-security/encode/
date: 2021-01-11
key: Java.C.Certificate-java-security
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Certificate-java-security.metodos valor="encode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void encode(OutputStream stream) throws KeyException, IOException
~~~

## Parámetros
* **OutputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream stream" %}

## Excepciones
[KeyException](/Java/KeyException/), [IOException](/Java/IOException/)

## Clase Padre
[Certificate](/Java/Certificate-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
