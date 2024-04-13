---
title: SSLSocket.setHandshakeApplicationProtocolSelector()
permalink: /Java/SSLSocket/setHandshakeApplicationProtocolSelector/
date: 2021-01-11
key: Java.S.SSLSocket
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSocket.metodos valor="setHandshakeApplicationProtocolSelector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setHandshakeApplicationProtocolSelector(BiFunction<SSLSocket,List<String>,String> selector)
~~~

## Parámetros
* **List&lt;String&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="List<String>" %}
* **String&gt; selector**,  {% include w3api/param_description.html metodo=_dato parametro="String> selector" %}
* **BiFunction&lt;SSLSocket**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<SSLSocket" %}

## Clase Padre
[SSLSocket](/Java/SSLSocket/)

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
