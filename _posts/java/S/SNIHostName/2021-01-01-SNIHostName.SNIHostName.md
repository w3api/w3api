---
title: SNIHostName.SNIHostName()
permalink: /Java/SNIHostName/SNIHostName/
date: 2021-01-11
key: Java.S.SNIHostName
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SNIHostName.constructores valor="SNIHostName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SNIHostName(byte[] encoded)
public SNIHostName(String hostname)
~~~

## Parámetros
* **String hostname**,  {% include w3api/param_description.html metodo=_dato parametro="String hostname" %}
* **byte[] encoded**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] encoded" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SNIHostName](/Java/SNIHostName/)

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
