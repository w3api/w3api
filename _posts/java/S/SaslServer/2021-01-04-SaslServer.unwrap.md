---
title: SaslServer.unwrap()
permalink: Java/SaslServer/unwrap
date: 2021-01-04
key: JavaJava.S.SaslServer
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslServer.metodos valor="unwrap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] unwrap(byte[] incoming, int offset, int len) throws SaslException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] incoming**,  {% include w3api/param_description.html metodo=_data parametro="byte[] incoming" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[SaslException](/Java/SaslException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[SaslServer](/Java/SaslServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
