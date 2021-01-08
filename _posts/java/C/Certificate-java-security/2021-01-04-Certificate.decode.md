---
title: Certificate.decode()
permalink: Java/Certificate-java-security/decode
date: 2021-01-04
key: JavaJava.C.Certificate-java-security
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Certificate-java-security.metodos valor="decode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void decode(InputStream stream) throws KeyException, IOException
~~~

## Parámetros
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}

## Excepciones
[KeyException](/Java/KeyException/), [IOException](/Java/IOException/)

## Clase Padre
[Certificate](/Java/Certificate-java-security/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Certificate-java-security.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
