---
title: SSLEngine.setHandshakeApplicationProtocolSelector()
permalink: Java/SSLEngine/setHandshakeApplicationProtocolSelector
date: 2021-01-04
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="setHandshakeApplicationProtocolSelector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setHandshakeApplicationProtocolSelector(BiFunction<SSLEngine,List<String>,String> selector)
~~~

## Parámetros
* **BiFunction&lt;SSLEngine**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<SSLEngine" %}
* **List&lt;String&gt;**,  {% include w3api/param_description.html metodo=_data parametro="List<String>" %}
* **String&gt; selector**,  {% include w3api/param_description.html metodo=_data parametro="String> selector" %}

## Clase Padre
[SSLEngine](/Java/SSLEngine/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
