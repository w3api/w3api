---
title: SNIServerName.SNIServerName()
permalink: Java/SNIServerName/SNIServerName
date: 2021-01-04
key: JavaJava.S.SNIServerName
category: java
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
* **byte[] encoded**,  {% include w3api/param_description.html metodo=_data parametro="byte[] encoded" %}
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SNIServerName](/Java/SNIServerName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SNIServerName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
