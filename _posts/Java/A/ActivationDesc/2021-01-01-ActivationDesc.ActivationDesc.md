---
title: ActivationDesc.ActivationDesc()
permalink: /Java/ActivationDesc/ActivationDesc/
date: 2021-01-11
key: Java.A.ActivationDesc
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationDesc.constructores valor="ActivationDesc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ActivationDesc(String className, String location, MarshalledObject<?> data) throws ActivationException
public ActivationDesc(String className, String location, MarshalledObject<?> data, boolean restart) throws ActivationException
public ActivationDesc(ActivationGroupID groupID, String className, String location, MarshalledObject<?> data)
public ActivationDesc(ActivationGroupID groupID, String className, String location, MarshalledObject<?> data, boolean restart)
~~~

## Parámetros
* **ActivationGroupID groupID**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID groupID" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}
* **boolean restart**,  {% include w3api/param_description.html metodo=_dato parametro="boolean restart" %}
* **String location**,  {% include w3api/param_description.html metodo=_dato parametro="String location" %}
* **MarshalledObject&lt;?&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject<?> data" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ActivationDesc](/Java/ActivationDesc/)

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
