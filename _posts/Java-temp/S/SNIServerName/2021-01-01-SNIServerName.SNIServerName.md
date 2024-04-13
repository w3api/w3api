---
title: SNIServerName.SNIServerName()
permalink: /Java/SNIServerName/SNIServerName/
date: 2021-01-11
key: Java.S.SNIServerName
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SNIServerName.constructores valor="SNIServerName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SNIServerName(int type, byte[] encoded)
~~~

## Parámetros
* **byte[] encoded**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] encoded" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SNIServerName](/Java/SNIServerName/)

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
