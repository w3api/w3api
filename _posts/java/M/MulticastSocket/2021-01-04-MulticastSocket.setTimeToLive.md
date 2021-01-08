---
title: MulticastSocket.setTimeToLive()
permalink: Java/MulticastSocket/setTimeToLive
date: 2021-01-04
key: JavaJava.M.MulticastSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="setTimeToLive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTimeToLive(int ttl) throws IOException
~~~

## Parámetros
* **int ttl**,  {% include w3api/param_description.html metodo=_data parametro="int ttl" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[MulticastSocket](/Java/MulticastSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MulticastSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
