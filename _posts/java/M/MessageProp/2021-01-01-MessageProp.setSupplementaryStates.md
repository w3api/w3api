---
title: MessageProp.setSupplementaryStates()
permalink: Java/MessageProp/setSupplementaryStates
date: 2021-01-11
key: JavaJava.M.MessageProp
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageProp.metodos valor="setSupplementaryStates" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSupplementaryStates(boolean duplicate, boolean old, boolean unseq, boolean gap, int minorStatus, String minorString)
~~~

## Parámetros
* **boolean old**,  {% include w3api/param_description.html metodo=_dato parametro="boolean old" %}
* **boolean unseq**,  {% include w3api/param_description.html metodo=_dato parametro="boolean unseq" %}
* **boolean duplicate**,  {% include w3api/param_description.html metodo=_dato parametro="boolean duplicate" %}
* **boolean gap**,  {% include w3api/param_description.html metodo=_dato parametro="boolean gap" %}
* **int minorStatus**,  {% include w3api/param_description.html metodo=_dato parametro="int minorStatus" %}
* **String minorString**,  {% include w3api/param_description.html metodo=_dato parametro="String minorString" %}

## Clase Padre
[MessageProp](/Java/MessageProp/)

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
