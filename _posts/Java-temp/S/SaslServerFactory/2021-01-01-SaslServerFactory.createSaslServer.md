---
title: SaslServerFactory.createSaslServer()
permalink: /Java/SaslServerFactory/createSaslServer/
date: 2021-01-11
key: Java.S.SaslServerFactory
category: Java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslServerFactory.metodos valor="createSaslServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SaslServer createSaslServer(String mechanism, String protocol, String serverName, Map<String,?> props, CallbackHandler cbh) throws SaslException
~~~

## Parámetros
* **CallbackHandler cbh**,  {% include w3api/param_description.html metodo=_dato parametro="CallbackHandler cbh" %}
* **?&gt; props**,  {% include w3api/param_description.html metodo=_dato parametro="?> props" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **String serverName**,  {% include w3api/param_description.html metodo=_dato parametro="String serverName" %}
* **String mechanism**,  {% include w3api/param_description.html metodo=_dato parametro="String mechanism" %}

## Excepciones
[SaslException](/Java/SaslException/)

## Clase Padre
[SaslServerFactory](/Java/SaslServerFactory/)

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
