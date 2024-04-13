---
title: X509ExtendedKeyManager.chooseEngineServerAlias()
permalink: /Java/X509ExtendedKeyManager/chooseEngineServerAlias/
date: 2021-01-11
key: Java.X.X509ExtendedKeyManager
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509ExtendedKeyManager.metodos valor="chooseEngineServerAlias" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String chooseEngineServerAlias(String keyType, Principal[] issuers, SSLEngine engine)
~~~

## Parámetros
* **Principal[] issuers**,  {% include w3api/param_description.html metodo=_dato parametro="Principal[] issuers" %}
* **SSLEngine engine**,  {% include w3api/param_description.html metodo=_dato parametro="SSLEngine engine" %}
* **String keyType**,  {% include w3api/param_description.html metodo=_dato parametro="String keyType" %}

## Clase Padre
[X509ExtendedKeyManager](/Java/X509ExtendedKeyManager/)

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
