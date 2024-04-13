---
title: JMXConnectorServer.connectionFailed()
permalink: /Java/JMXConnectorServer/connectionFailed/
date: 2021-01-11
key: Java.J.JMXConnectorServer
category: Java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXConnectorServer.metodos valor="connectionFailed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void connectionFailed(String connectionId, String message, Object userData)
~~~

## Parámetros
* **Object userData**,  {% include w3api/param_description.html metodo=_dato parametro="Object userData" %}
* **String connectionId**,  {% include w3api/param_description.html metodo=_dato parametro="String connectionId" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXConnectorServer](/Java/JMXConnectorServer/)

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
